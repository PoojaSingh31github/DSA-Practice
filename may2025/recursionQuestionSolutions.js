// 1. Flatten nested tree labels
// - Description: Extract all `label` values from nested tree objects.
// - Input: const navTree = { label: 'Home', children: [ { label: 'Products', children: [ {
// - Output: ['Home','Products','Electronics','Mobile']



// 2. Count total nodes in nested tree
// - Description: Count all objects including children recursively.
// - Input: navTree (same as above)
// - Output: 4



// 3. Flatten deeply nested array using recursion
// - Description: Convert [1,[2,[3,[4]]]] → [1,2,3,4]
// - Input: [1,[2,[3,[4]]]]
// - Output: [1,2,3,4]
// 4. Sum all numbers in nested object
// - Description: Sum all numeric values in nested objects.
// - Input: {a:1, b:{c:2,d:{e:3}}}
// - Output: 6
// 5. Transform flat array to nested tree
// - Description: Convert flat array with id and parentId into nested tree.
// - Input: [{id:1,parentId:null,label:'Home'},{id:2,parentId:1,label:'Products'},{id:3,pare
// - Output: nested tree object with hierarchy
// 6. Extract all keys from nested object
// - Description: Recursively list all keys in a flat array.
// - Input: {a:1, b:{c:2, d:{e:3}}}
// - Output: ['a','b','c','d','e']
// Output: Expected transformed output for question {i}""")
// Add to PDF
// Build PDF
// 7. Group objects by property recursively
// - Description: Group array of objects and their children by a property.
// - Input: [{type:'a', children:[{type:'b'}]},{type:'a', children:[{type:'a'}]}]
// - Output: {a:[{type:'a'},{type:'a'}], b:[{type:'b'}]}
// 8. Sum numbers in nested arrays recursively
// - Description: Sum all numbers inside nested arrays.
// - Input: [1,[2,[3,4],5],6]
// - Output: 21
// 9. Object to key-value array recursively
// - Description: Convert nested object to array of [key,value] pairs, flatten keys with dot
// - Input: {a:1,b:{c:2}}
// - Output: [['a',1],['b.c',2]]
// 10. Flatten menu tree to breadcrumb paths
// - Description: Return all breadcrumb style paths as strings from root to leaves.
// - Input: navTree (from #1)
// - Output: ['Home','Home > Products','Home > Products > Electronics','Home > Products > El
// 11. Filter nested objects by key-value
// - Description: Return all objects where a key matches a value, recursively.
// - Input: [{id:1,type:'a',children:[{id:2,type:'b'}]},{id:3,type:'a'}]
// - Output: [{id:1,type:'a',...},{id:3,type:'a'}]
// 12. Find max depth of nested objects
// - Description: Determine maximum nested depth in an object or array.
// - Input: {a:{b:{c:{d:1}}}}
// - Output: 4
// 13. Merge multiple nested objects deeply
// - Description: Deep merge two objects combining properties recursively.
// - Input: {a:1,b:{c:2}}, {b:{d:3}, e:4}
// - Output: {a:1,b:{c:2,d:3}, e:4}
// 14. Remove keys with null or undefined recursively
// - Description: Return object with no keys that have null/undefined values in any depth.
// - Input: {a:null,b:{c:2,d:null}}
// - Output: {b:{c:2}}
// 15. Count all leaves in nested tree
// - Description: Count all nodes with no children in nested objects.
// - Input: navTree (see #1)
// - Output: 1 (Mobile node)
// 16. Flatten nested arrays to single level and unique
// - Description: Flatten nested arrays and remove duplicates.
// - Input: [1,[2,[2,3],3],1]
// - Output: [1,2,3]
// 17. Invert keys and values in nested object (leaves only)
// - Description: Swap keys and values recursively for leaf nodes.
// - Input: {a:1, b:{c:2}}
// - Output: {1:'a', b:{2:'c'}}
// 18. Find all paths to target key
// - Description: Return all paths in nested object where key exists.
// - Input: {a:{b:{c:1}}, d:{c:2}}
// - Output: ['a.b.c', 'd.c']
// 19. Filter array of objects by nested property value
// - Description: Filter objects where nested property matches a condition.
// - Input: [{id:1,info:{type:'a'}},{id:2,info:{type:'b'}}]
// - Output: [{id:1,info:{type:'a'}}]
// 20. Sum all numeric values in nested arrays and objects
// - Description: Combine sums from nested arrays and objects.
// - Input: {a:[1,2], b:{c:3,d:[4,5]}}
// - Output: 15
// 21. Flatten nested object to query string
// - Description: Convert nested object to URL query parameters with dot notation.
// - Input: {a:1,b:{c:2}}
// - Output: "a=1&b.c=2"
// 22. Build nested object from flat dot notation keys
// - Description: Convert { 'a.b':1, 'a.c':2 } to {a:{b:1,c:2}}
// - Input: { 'a.b':1, 'a.c':2 }
// - Output: {a:{b:1,c:2}}
// 23. Find first leaf node in nested tree
// - Description: Return the first leaf node value.
// - Input: navTree (see #1)
// - Output: 'Mobile'
// 24. Recursive clone of an object or array
// - Description: Deep copy an object or array recursively.
// - Input: {a:1,b:{c:2}}
// - Output: exact deep copy
// 25. Remove duplicate objects from nested arrays by key
// - Description: Remove duplicates by key in nested arrays.
// - Input: [{id:1},{id:2},{id:1}]
// - Output: [{id:1},{id:2}]
// 26. Update all nested values by key
// - Description: Increment all values where key is 'count' in
// - Description: Increment all values where key is 'count' in nested objects.
// - Input: {count:1, nested:{count:2}}
// - Output: {count:2, nested:{count:3}}
// 27. Convert array of objects to lookup map by id recursively
// - Description: Transform nested arrays to id-keyed map.
// - Input: [{id:1, children:[{id:2}]}]
// - Output: {1:..., 2:...}
// 28. Find duplicate keys in nested objects
// - Description: Return array of keys repeated in nested objects.
// - Input: {a:1,b:{a:2}}
// - Output: ['a']
// 29. Generate array of all leaf node values
// - Description: Extract leaf node values from nested objects/arrays.
// - Input: {a:1,b:{c:2,d:3}}
// - Output: [1,2,3]
// 30. Replace all values of a key recursively
// - Description: Replace all values of 'status' key in nested objects with 'done'.
// - Input: {status:'pending', nested:{status:'pending'}}
// - Output: {status:'done', nested:{status:'done'}}
// 31. Filter out empty arrays/objects recursively
// - Description: Remove empty arrays or objects deeply.
// - Input: {a:[], b:{c:{}}}
// - Output: {}
// 32. Get count of each unique value in nested arrays
// - Description: Count occurrences of each value flattening nested arrays.
// - Input: [1,[2,1,[2,3]]]
// - Output: {1:2, 2:2, 3:1}
// 33. Find and replace in nested string properties
// - Description: Replace substring in all nested string values.
// - Input: {a:'foo', b:{c:'foobar'}}
// - Output: {a:'bar', b:{c:'barbar'}}
// 34. Group and count nested objects by property
// - Description: Count items grouped by type recursively.
// - Input: [{type:'a', children:[{type:'b'}]}, {type:'a'}]
// - Output: {a:2, b:1}
// 35. Convert nested arrays to tree structure
// - Description: Transform nested array of ids into nested tree form.
// - Input: [[1,[2]], 3]
// - Output: tree object with children
// 36. Map nested objects to different structure
// - Description: Rename 'label' keys to 'name' throughout nested object.
// - Input: {label:'a', children:[{label:'b'}]}
// - Output: {name:'a', children:[{name:'b'}]}
// 37. Calculate product of all numbers in nested arrays
// - Description: Multiply all numbers in nested arrays.
// - Input: [1,[2,[3]]]
// - Output: 6
// 38. Flatten nested array of objects with specific key
// - Description: Collect all objects of a certain type recursively.
// - Input: [{type:'a', children:[{type:'b'}]}, {type:'a'}]
// - Output: [{type:'a'}, {type:'b'}, {type:'a'}]
// 39. Remove specific key from nested objects
// - Description: Delete all occurrences of key 'password' recursively.
// - Input: {user:'x', password:'123', nested:{password:'abc'}}
// - Output: {user:'x', nested:{}}
// 40. Extract nested values by path array
// - Description: Given path ['a','b'], get value from nested object.
// - Input: {a:{b:2}}
// - Output: 2
// 41. Find minimum numeric value in nested object
// - Description: Return smallest number in nested objects.
// - Input: {a:10, b:{c:5, d:7}}
// - Output: 5
// 42. Replace null values in nested object with default
// - Description: Fill null or undefined with default value.
// - Input: {a:null, b:{c:undefined}}
// - Output: {a:'default', b:{c:'default'}}
// 43. Sort nested arrays by key recursively
// - Description: Sort arrays by 'name' key inside nested objects.
// - Input: [{name:'b'}, {name:'a', children:[{name:'c'}]}]
// - Output: sorted arrays at all levels
// 44. Validate nested structure shape
// - Description: Check if nested object contains keys a,b,c at all levels.
// - Input: {a:1,b:2,c:3, d:{a:1,b:2,c:3}}
// - Output: true
// 45. Calculate average of numbers in nested arrays/objects
// - Description: Return average number from all nested numeric values
// - Description: Return average number from all nested numeric values.
// - Input: {a:1,b:[2,3], c:{d:4}}
// - Output: 2.5
// 46. Strip HTML tags from nested string properties
// - Description: Remove HTML markup in all nested string values.
// - Input: {html:'<b>bold</b>', nested:{html:'<i>italic</i>'}}
// - Output: {html:'bold', nested:{html:'italic'}}
// 47. Generate nested object structure from array of paths
// - Description: Create object from array like [['a','b'], ['a','c']]
// - Input: [['a','b'], ['a','c']]
// - Output: {a:{b:{}, c:{}}}
// 48. Deep freeze nested objects recursively
// - Description: Make object and all nested children immutable.
// - Input: {a:1, b:{c:2}}
// - Output: deeply frozen object
// 49. Count words in nested string properties
// - Description: Sum word counts in all nested string leaves.
// - Input: {text:'hello world', nested:{text:'foo bar'}}
// - Output: 4
// 50. Generate CSS selector string from nested style object
// - Description: Flatten nested CSS properties to selector strings.
// - Input: {'.btn':{color:'red', ':hover':{color:'blue'}}}
// - Output: ['.btn {color:red}', '.btn:hover {color:blue}']
