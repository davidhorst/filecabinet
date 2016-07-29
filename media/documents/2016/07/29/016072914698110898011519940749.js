distances = [
    [0,  26, 29, 11, 8, 25, 49, 4, 33, 42, 50, 27, 11, 33, 5, 4, 8, 21, 30, 49],
    [26,  0, 24, 19, 21, 3, 25, 12, 36, 7, 46, 8, 18, 9, 42, 50, 12, 16, 38, 39],
    [29, 24,  0, 17, 43, 25, 42, 46, 31, 49, 9, 9, 13, 30, 33, 28, 9, 5, 21, 42],
    [11, 19, 17, 0, 49, 7, 21, 49, 17, 18, 29, 10, 41, 12, 4, 35, 49, 7, 44, 38],
    [8,  21, 43, 49, 0, 12, 30, 29, 35, 50, 37, 45, 3, 40, 47, 32, 9, 34, 22, 42],
    [25,  3, 25, 7, 12, 0, 36, 12, 6, 36, 14, 2, 42, 18, 39, 19, 15, 37, 28, 5],
    [49, 25, 42, 21, 30, 36, 0, 12, 17, 24, 22, 20, 16, 29, 46, 30, 34, 5, 38, 9],
    [4,  12, 46, 49, 29, 12, 12, 0, 26, 19, 41, 28, 40, 36, 30, 12, 4, 38, 46, 27],
    [33, 36, 31, 17, 35, 6, 17, 26, 0, 27, 24, 44, 33, 46, 23, 22, 30, 35, 36, 19],
    [42,  7, 49, 18, 50, 36, 24, 19, 27, 0, 3, 6, 32, 27, 18, 43, 33, 45, 26, 31],
    [50, 46,  9, 29, 37, 14, 22, 41, 24, 3, 0, 44, 43, 47, 26, 28, 20, 12, 6, 24],
    [27,  8,  9, 10, 45, 2, 20, 28, 44, 6, 44, 0, 6, 3, 33, 25, 9, 12, 5, 46],
    [11, 18, 13, 41, 3, 42, 16, 40, 33, 32, 43, 6, 0, 36, 47, 17, 31, 21, 3, 38],
    [33,  9, 30, 12, 40, 18, 29, 36, 46, 27, 47, 3, 36, 0, 1, 5, 23, 32, 49, 20],
    [5,  42, 33, 4, 47, 39, 46, 30, 23, 18, 26, 33, 47, 1, 0, 2, 7, 48, 5, 43],
    [4,  50, 28, 35, 32, 19, 30, 12, 22, 43, 28, 25, 17, 5, 2, 0, 18, 28, 35, 50],
    [8,  12,  9, 49, 9, 15, 34, 4, 30, 33, 20, 9, 31, 23, 7, 18, 0, 27, 44, 23],
    [21, 16,  5, 7, 34, 37, 5, 38, 35, 45, 12, 12, 21, 32, 48, 28, 27, 0, 5, 30],
    [30, 38, 21, 44, 22, 28, 38, 46, 36, 26, 6, 5, 3, 49, 5, 35, 44, 5, 0, 49],
    [49, 39, 42, 38, 42, 5, 9, 27, 19, 31, 24, 46, 38, 20, 43, 50, 23, 30, 49, 0],
    ]

 //console.log(distances)
 
function greedy_basic(start, matrix) {
 	
 	var bc = [];       // create a "breadcrumb" based on the size of matrix
 	var path =[];      // track the path
 	var distance = 0;  // distance sum
 	
 	for(var i=0; i<matrix.length; i++) { // insert true to bc, as in haven't hit any cities yet
 		bc.push(true);
 	}
 
 	var currentCity = start;
 	bc[start]=false;   // set start bc to false
 	
 	for(var j=0; j<matrix.length; j++) { // iterate through the cities
 		
 		var shortestPath = null;
 		for(var k=0; k<matrix.length; k++) { // find the shortest distance
 			if(bc[k]){
 				if(shortestPath === null || matrix[currentCity][k] < matrix[currentCity][shortestPath]) {
 					shortestPath = k;
 				}
 			}
 		}
 		if(shortestPath === null) { // iterated though all cities, go back to start
 			distance += matrix[currentCity][start];
 			path.push(start);
 		} else {
 			distance += matrix[currentCity][shortestPath];
 			path.push(shortestPath);
 			currentCity = shortestPath;
 			bc[currentCity] = false;
 		}
 		
 	}
 	return [distance, path]
 }
 
 function greedy_basic_start_from_all(matrix) {
 	var best = greedy_basic(0,matrix);
 	for(var i=1; i<matrix.length; i++) { // iterate through all cities as starting point and pick the best
 		var temp = greedy_basic(i,matrix);
 		if (temp[0] < best[0]) {
 			best = temp;
 		}
 	}
 	return temp;
 }
 
function randomPath(trial, matrix) {
	var shortestD = null;
	var shortestP;
	for(var i=0; i<trial; i++){
		var path = getRandomPath(matrix.length);
		var dist = calcDistance(path, matrix);
		if(shortestD === null || dist < shortestD ) {
			shortestD = dist;
			shortestP = path;
		}
	}
	return [shortestD, shortestP];
}

function calcDistance(path, matrix) { // HELPER
	var d = 0;
	for (var i=0; i<path.length; i++) {
		d += matrix[path[i]][path[(i+1)%(path.length-1)]];
	}
	return d;
}
function getRandomPath(len) { // HELPER
	var randomPath = [];
	var tempArr = []
    for (var i = 0; i < len; i++) {
        tempArr.push(i);
    }
	for (var j = 0; j < len; j++) {
	    var index = Math.floor(Math.random() * tempArr.length);
	    var val = tempArr[index];
	    randomPath.push(tempArr.splice(index, 1)[0]);
	}
    return randomPath;
}	
 
console.log(greedy_basic(0,distances)); // greedy_basic from a single point
console.log(greedy_basic_start_from_all(distances)); // greedy_basic from a single point

var date = new Date();
var start = date.getTime(); 
console.log(start);
console.log(randomPath(1000000000, distances));
var date = new Date();
var end = date.getTime();
console.log(end);

var seconds = (end - start);
console.log(seconds);
