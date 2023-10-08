#include <bits/stdc++.h>

using namespace std;

class solve_stack{
public:
    void insert(int price){
        if(s.empty()){
            s.push({price , 1});
            cout << 1 << '\n';
        }
        else{
            int counter = 1;
            while(s.top().first <= price){
                counter += s.top().second;
                s.pop();
            }
            s.push({price , counter});
            cout << counter << '\n';
        }
    }

private:
    stack<pair<int ,int> > s;
};

class solve_dq{
public:
    int solve(vector<int> &v , int limit){
        deque<int> minim , maxim;
        int lo = 0 , hi , ans = 1;
        for(hi = 0; hi < v.size(); hi++){
            while(!maxim.empty() && maxim.back() <= v[hi]){
                maxim.pop_back();
            }
            maxim.push_back(v[hi]);

            while(!minim.empty() && minim.back() >= v[hi]){
                minim.pop_back();
            }
            minim.push_back(v[hi]);

            if(maxim.front() - minim.front() > limit){
                if(maxim.front() == v[lo]){
                    maxim.pop_front();
                }
                if(minim.front() == v[lo]){
                    minim.pop_front();
                }
                lo++;
            }
            ans = max(ans , hi - lo + 1);
        }
        return ans;
    }
};
