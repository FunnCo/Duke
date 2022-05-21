# Этот класс представляет ориентированный граф
# используя матрицу пропускных способностей
class Graph:

    # Конструктор, с параметром в виде матрицы пропускных способностей
    def __init__(self, graph):
        self.graph = graph  
        self.ROW = len(graph)


    '''Возвращает true если существует путь из источника 's' в сток 't' в
    остаточном графе. Также заполняет parent[] для хранения пути '''
    def BFS(self, s, t, parent):

        # Объявление всех вершин непосещенными
        visited = [False] * self.ROW

        # Объявление очереди для поиска
        queue = [s]

        # Отметка о посещении вершины с источником
        visited[s] = True

        # Цикл поиска в ширину
        while queue:

            # Получение следующей вершины из очереди
            u = queue.pop(0)

            # Получение всех смежных вершин с взятой из очереди
            # Если смежная вершина не была посещена, тогда она отмечается
            # посещенной и добавляется в очередь
            for ind, val in enumerate(self.graph[u]):
                if visited[ind]==False and val > 0:
                    # Если будет найден путь в сток
                    # тогда поиск больше не имеет значения.
                    # В таком случае необходимо установить его родительский элемент и вернуть true
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        # Путь в сток из источника не был найден
        # Значит необходимо вернуть false
        return False

    # Возвращает значение максимального потока из s в t в заданном графе
    def FordFulkerson(self, source, sink):

        # Этот массив заполняется в BFS (поиск в ширину) и хранит путь
        parent = [-1] * self.ROW

        # Изначально потока нет
        max_flow = 0 

        # Увеличение значения потока, пока есть путь из источника в сток
        while self.BFS(source, sink, parent):

            # Найти максимальный поток в найденном пути
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Добавить поток в данном пути в общий поток
            max_flow += path_flow

            # Обновление остаточных емкостей вершин их их инверсирование вдоль пути
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


def solve_max_flow(graph, source, sink):
    if source==sink:
        return "Некорректный ввод! Источник и сток одинаковы!"
    g = Graph(graph)
    result = g.FordFulkerson(source, sink)
    if not result == 0:
        return result
    else:
        return "Нет потока!"
