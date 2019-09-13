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
Package orderedmap implements an insertion-ordered associative array, also
called map or dictionary. Maps are an abstract data type that can hold data in
(key, value) pairs.

Associative arrays have two imporant properties. Every key can only appear
once, and, every key can only have one value.

An insertion-ordered map have the extra property that when it is iterated it
returns their values in order they where inserted originally.

Example

	package main

	import (
		"github.com/goombaio/orderedmap"
	)

	func main() {
		m := orderedmap.NewOrderedMap()
		m.Put("one", "First element")
		m.Put("two", "Second element")
		m.Put("three", "Last element")

		for _, entry := range m.Values() {
			fmt.Println(entry)
		}
		// Output:
		// First element
		// Second element
		// Last element
	}
*/
package orderedmap
