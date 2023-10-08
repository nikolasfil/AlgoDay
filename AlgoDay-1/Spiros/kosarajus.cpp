class graph{
public:
    graph(int V , int E) : V(V) , E(E) {}

    void addEdge(int a , int b){
        adj[a].push_back(b);
        //adj[b].push_back(a);
    }

    void dfs(int start){
        vector<bool> visited(V , false);
        visited[start] = true;
        stack<int> s;
        s.push(start);
        while(!s.empty()){
            int current = s.top();
            visited[current] = true;
            s.pop();
            for(auto & x : adj[current]){
                if(!visited[x]){
                    s.push(x);
                }
            }
        }
    }

    void bfs(int start){
        vector<bool> visited(V , false);
        visited[start] = true;
        queue<int> q;
        q.push(start);
        while(!q.empty()){
            auto current = q.front();
            visited[current] = true;
            q.pop();
            for(auto & x : adj[current]){
                if(!visited[x]){
                    q.push(x);
                }
            }
        }
    }

    void dfs_2(vector<bool> &visited , int start){
        visited[start] = true;
        for(auto & x : adj[start]){
            if(!visited[x]){
                dfs_2(visited , x);
            }
        }
    }


    int islands(int start){
        int counter = 0;
        vector<bool> visited(V , false);
        for(int i = 0; i<V; i++){
            if(!visited[i]) {
                dfs_2(visited, i);
                counter++;
            }
        }
        return counter;
    }

    void push_vertex(int start , stack<int> &s , vector<bool> &visited){
        visited[start] = true;
        for(auto & x : adj[start]){
            if(!visited[x]){
                push_vertex(x , s , visited);
            }
        }

        s.push(start);
    }

    void dfs_with_new(vector<bool> &visited,  int start , unordered_map<int , vector<int> > &adj){
        visited[start] = true;
        for(auto & x : adj[start]){
            if(!visited[x]){
                dfs_with_new(visited , x , adj);
            }
        }
    }

    int kosaraju(){
        vector<bool> visited(V , false);
        stack<int> s;
        for(int i = 0; i<V; i++){
            if(!visited[i]){
                push_vertex(i , s , visited);
            }
        }
        //φτιάχνω τον καινουργιο γράφο
        unordered_map<int , vector<int> > new_adj;
        for(int i = 0; i<V; i++){
            for(auto & x : adj[i]){
                new_adj[x].push_back(i);
            }
        }

        //2ο πέρασμα
        int scc = 0;
        for(int i = 0; i<V; i++){
            visited[i] = false;
        }
        while(!s.empty()) {
            int current = s.top();
            s.pop();
            if (!visited[current]) {
                dfs_with_new(visited, current, new_adj);
                scc++;
            }
        }
        return scc;
    }

private:
    unordered_map<int , vector<int> > adj;
    int V;
    int E;
};


int main(){
    int V , E; cin >> V >> E;
    graph g(V , E);
    while(E--) {
        int a, b;
        cin >> a >> b;
        g.addEdge(a , b);
    }
    cout << g.kosaraju() << '\n';
}
