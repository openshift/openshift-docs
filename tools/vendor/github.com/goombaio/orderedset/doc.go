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

/*
Package orderedset implements a dynamic, insertion-ordered, set abstract data
type. A set is an abstract data type that can store unique values.

Curent implementation

	* Is a dynamic set.
	  It implements actions to Add() or Remove() elements from it among others.
	* Is ordered.
	  Instead the generic set, this implementation is insertion ordered,
	  meaning that when iterating over its elements, it will return them in
	  order they where inserted originally.

Example

	package main

	import (
		"github.com/goombaio/orderedset"
	)

	func main() {
		s := orderedset.NewOrderedSet()
		s.Add("First element")
		s.Add("Second element")
		s.Add("Last element")

		for _, entry := range s.Values() {
			fmt.Println(entry)
		}
		// Output:
		// First element
		// Second element
		// Last element
	}
*/
package orderedset
