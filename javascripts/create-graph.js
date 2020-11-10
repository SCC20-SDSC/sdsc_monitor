/*
 * Parse the data and create a graph with the data.
 */
function parseData(createGraph) {
	Papa.parse("./data.csv", {
		download: true,
		complete: function(results) {
			createGraph(results.data);
		}
	});

}

function createGraph(data) {


	var times = [];
	var ans = [];
	var mation = [];
	for (var i = 1; i < data[0].length; i++){
		k = [];
		k.push(data[0][i]);
		ans.push(k);
		v = [];
		v.push(data[0][i] + 'total');
		mation.push(v);
	}
	console.log(mation);
	//i row p col
	for (var p = 0; p < data[0].length - 1; p++){
		sums = 0
		for (var i = 1; i < data.length-1; i++) {
			if(p == 0){
				times.push(data[i][0]);
			}
			f = p + 1;
			ans[p].push(data[i][f]);
			mation[p].push(sums/10);
			sums += parseFloat(data[i][f])
			if(p == 0){
		}
			/*console.log(p)
			console.log(data[i][f]);*/
			}
		}
	console.log(ans);
	/*console.log(times);
	*/
	//console.log(times);
	//console.log(ans);

	var price = c3.generate({
		bindto: '#price',
	    data: {
	        columns: ans
	    },
			grid: {
				x: {
						show: true
				},
				y: {
						show: true
				}
			},
			zoom: {
			 enabled: true
		 	},
	    axis: {
	        x: {
	            type: 'category',
	            categories: times,
	            tick: {
	            	multiline: false,
                	culling: {
                    	max: 5
                	}
            	}
	        }
	    },
	    zoom: {
        	enabled: true
    	},
	    legend: {
	        position: 'right'
	    }
	});


	var cost = c3.generate({
		bindto: '#cost',
	    data: {
	        columns: mation,
	        types: {
	        }
	    },
			grid: {
				x: {
						show: true
				},
				y: {
						show: true
				}
			},
			axis: {
					x: {
							type: 'category',
							categories: times,
							tick: {
								multiline: false,
									culling: {
											max: 5
									}
							}
					}
			},
			zoom: {
			 enabled: true
		 	},
	});
	cost.transform('area');








}

parseData(createGraph);
