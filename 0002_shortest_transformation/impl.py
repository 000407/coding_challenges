import sys

def solution(startWord, endWord, wordList):
	if endWord not in wordList:
		return 0

	if startWord not in wordList:
		wordList.append(startWord)

	delta_1_graph = make_graph(wordList)
	
	return dijkstra_shortest_path(delta_1_graph, startWord, endWord)


def make_graph(wordList):
	graph = dict()

	for word in wordList:
		graph[word] = [w for w in wordList if sum(a != b for a, b in zip(word, w)) == 1]

	return graph


def dijkstra_shortest_path(graph, start, end):
	g_dist = {w: (sys.maxsize, None) for w in graph.keys()}
	g_dist[start] = (0, None)

	l_unvisited = set(graph.keys())

	while len(l_unvisited) != 0:
		word = get_min_dist_v(g_dist, l_unvisited)

		for aw in graph[word]:
			dist = g_dist[word][0] + 1
			
			if dist < g_dist[aw][0]:
				g_dist[aw] = (dist, word)
		
		l_unvisited.remove(word)

	return g_dist[end][0]


def get_min_dist_v(g_dist, l_unvisited):
	min_k = None
	min_d = sys.maxsize

	for w in l_unvisited:
		if g_dist[w][0] < min_d:
			min_d = g_dist[w][0]
			min_k = w

	return min_k


def main():
	word_list = ['hat', 'dog', 'dig', 'tig', 'cog', 'hot', 'dot']

	print('hit -> cog', 'expected_dist: 4', solution('hit', 'cog', word_list) == 4)
	print('hot -> tig', 'expected_dist: 4', solution('hot', 'tig', word_list) == 4)
	print('hit -> tig', 'expected_dist: 5', solution('hit', 'tig', word_list) == 5)
	print('tig -> hat', 'expected_dist: 5', solution('tig', 'hat', word_list) == 5)


if __name__ == "__main__":
	main()