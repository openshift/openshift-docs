// Copyright 2018, Goomba project Authors. All rights reserved.
//
// Licensed to the Apache Software Foundation (ASF) under one or more
// contributor license agreements.  See the NOTICE file distributed with this
// work for additional information regarding copyright ownership.  The ASF
// licenses this file to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
// License for the specific language governing permissions and limitations
// under the License.

package orderedset

import (
	"fmt"
	"sync"

	"github.com/goombaio/orderedmap"
)

// OrderedSet represents a dynamic, insertion-ordered, set abstract data type.
type OrderedSet struct {
	// currentIndex keeps track of the keys of the underlying store.
	currentIndex int

	// mu Mutex protects data structures below.
	mu sync.Mutex

	// index is the Set list of keys.
	index map[interface{}]int

	// store is the Set underlying store of values.
	store *orderedmap.OrderedMap
}

// NewOrderedSet creates a new empty OrderedSet.
func NewOrderedSet() *OrderedSet {
	orderedset := &OrderedSet{
		index: make(map[interface{}]int),
		store: orderedmap.NewOrderedMap(),
	}

	return orderedset
}

// Add adds items to the set.
//
// If an item is found in the set it replaces it.
func (s *OrderedSet) Add(items ...interface{}) {
	for _, item := range items {
		if _, found := s.index[item]; found {
			continue
		}

		s.put(item)
	}
}

// Remove deletes items from the set.
//
// If an item is not found in the set it doesn't fails, just does nothing.
func (s *OrderedSet) Remove(items ...interface{}) {
	for _, item := range items {
		index, found := s.index[item]
		if !found {
			return
		}

		s.remove(index, item)
	}
}

// Contains return if set contains the specified items or not.
func (s *OrderedSet) Contains(items ...interface{}) bool {
	s.mu.Lock()
	defer s.mu.Unlock()

	for _, item := range items {
		if _, found := s.index[item]; !found {
			return false
		}
	}
	return true
}

// Empty return if the set in empty or not.
func (s *OrderedSet) Empty() bool {
	return s.store.Empty()
}

// Values return the set values in insertion order.
func (s *OrderedSet) Values() []interface{} {
	return s.store.Values()
}

// Size return the set number of elements.
func (s *OrderedSet) Size() int {
	return s.store.Size()
}

// String implements Stringer interface.
//
// Prints the set string representation, a concatenated string of all its
// string representation values in insertion order.
func (s *OrderedSet) String() string {
	return fmt.Sprintf("%s", s.Values())
}

// Put adds a single item into the set
func (s *OrderedSet) put(item interface{}) {
	s.mu.Lock()
	defer s.mu.Unlock()

	s.store.Put(s.currentIndex, item)
	s.index[item] = s.currentIndex
	s.currentIndex++
}

// remove deletes a single item from the test given its index
func (s *OrderedSet) remove(index int, item interface{}) {
	s.mu.Lock()
	defer s.mu.Unlock()

	s.store.Remove(index)
	delete(s.index, item)
}
