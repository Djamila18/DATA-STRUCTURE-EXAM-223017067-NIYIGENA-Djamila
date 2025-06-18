#include <iostream>
#include <cstring>  // for memcpy
using namespace std;

// --- Struct Definitions ---

struct Edge {
    int to;
    float weight;
};

struct Vertex {
    int id;
    Edge* edges;
    int edgeCount;
    int edgeCapacity;

    Vertex() : id(-1), edges(nullptr), edgeCount(0), edgeCapacity(0) {}

    void addEdge(int to, float weight) {
        if (edgeCount == edgeCapacity) {
            edgeCapacity = edgeCapacity == 0 ? 2 : edgeCapacity * 2;
            Edge* newEdges = new Edge[edgeCapacity];
            for (int i = 0; i < edgeCount; ++i)
                *(newEdges + i) = *(edges + i);  // pointer arithmetic
            delete[] edges;
            edges = newEdges;
        }
        *(edges + edgeCount) = Edge{to, weight};  // pointer arithmetic
        ++edgeCount;
    }

    void freeEdges() {
        delete[] edges;
        edges = nullptr;
        edgeCount = 0;
        edgeCapacity = 0;
    }
};

// --- Abstract Graph Interface ---

class Graph {
protected:
    Vertex* vertices;
    int vertexCount;
    int vertexCapacity;

public:
    Graph() : vertices(nullptr), vertexCount(0), vertexCapacity(0) {}

    virtual void addEdge(int from, int to, float weight) = 0;

    virtual ~Graph() {
        for (int i = 0; i < vertexCount; ++i)
            vertices[i].freeEdges();
        delete[] vertices;
    }

    void addVertex(int id) {
        if (findVertex(id) != -1) return; // already exists

        if (vertexCount == vertexCapacity) {
            vertexCapacity = vertexCapacity == 0 ? 2 : vertexCapacity * 2;
            Vertex* newVertices = new Vertex[vertexCapacity];
            for (int i = 0; i < vertexCount; ++i)
                newVertices[i] = vertices[i];
            delete[] vertices;
            vertices = newVertices;
        }

        vertices[vertexCount].id = id;
        ++vertexCount;
    }

    void removeVertex(int id) {
        int index = findVertex(id);
        if (index == -1) return;

        vertices[index].freeEdges();
        for (int i = index; i < vertexCount - 1; ++i)
            vertices[i] = vertices[i + 1];
        --vertexCount;
    }

    int findVertex(int id) const {
        for (int i = 0; i < vertexCount; ++i)
            if (vertices[i].id == id)
                return i;
        return -1;
    }

    Vertex* getVertex(int id) {
        int idx = findVertex(id);
        return (idx != -1) ? &vertices[idx] : nullptr;
    }

    void printGraph() {
        for (int i = 0; i < vertexCount; ++i) {
            cout << "Vertex " << vertices[i].id << ": ";
            for (int j = 0; j < vertices[i].edgeCount; ++j) {
                Edge* e = vertices[i].edges + j;
                cout << "(" << e->to << ", " << e->weight << ") ";
            }
            cout << endl;
        }
    }
};

// --- DirectedGraph Implementation ---

class DirectedGraph : public Graph {
public:
    void addEdge(int from, int to, float weight) override {
        addVertex(from);
        addVertex(to);
        getVertex(from)->addEdge(to, weight);
    }
};

// --- UnweightedGraph Implementation ---

class UnweightedGraph : public Graph {
public:
    void addEdge(int from, int to, float weight = 1.0f) override {
        addVertex(from);
        addVertex(to);
        getVertex(from)->addEdge(to, 1.0f);
        getVertex(to)->addEdge(from, 1.0f);  // Undirected: Add both ways
    }
};

// --- Usage Example ---

int main() {
    int graphCount = 2;
    Graph** graphs = new Graph*[graphCount];

    graphs[0] = new DirectedGraph();
    graphs[1] = new UnweightedGraph();

    // Directed graph
    graphs[0]->addEdge(1, 2, 5.0f);
    graphs[0]->addEdge(1, 3, 2.0f);
    graphs[0]->addEdge(2, 4, 3.0f);

    // Unweighted (undirected) graph
    graphs[1]->addEdge(10, 20, 1.0f);
    graphs[1]->addEdge(10, 30, 1.0f);
    graphs[1]->addEdge(20, 40, 1.0f);

    cout << "Directed Graph:\n";
    graphs[0]->printGraph();

    cout << "\nUnweighted Graph:\n";
    graphs[1]->printGraph();

    // Cleanup
    for (int i = 0; i < graphCount; ++i)
        delete graphs[i];
    delete[] graphs;

    return 0;
}
