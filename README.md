# Nashville Music Hackathon 2018

## Getting Started

To get started download the data set here: and create a local clone of this repository. 

This challenge uses Pandas, so make sure you run: 

```
pip install -r requirements.txt
```

## Challenge

Given a bipartite graph, you must write a function connected_components(filepath) that takes 
a filepath of a csv (format: node_x, node_y), computes the connected components, and
outputs to a new csv called "output.csv". (format: cluster_id, node_x, node_y).

For example, given the following input csv:

| node_x | node_y |
| -------| -------|
| 1      | 2      |
| 2      | 4      |
| 5      | 7      |
| 7      | 9      |
| 11     | 12     |


Your script should create the following output file, called "output.csv" using the "input.csv" provided.:

|   cluster_id  |	node_x  |	node_y  |
| ------------- | ------- | ------- |
|   1           |	1       |	2       |
|   1           |	2       |	4       |
|   5           |	5       |	7       |
|   5           |	7       |	9       |
|   11          |	11      |	12      |


## Testing Your Results:

To test your results, ...
