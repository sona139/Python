#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n, a, b;
	cin >> n >> a >> b;
	if(b == 1) {
		cout << "Yes" << endl;
		return ;
	}
	map<int, int> used;
	priority_queue<int, vector<int> > q;
	q.push(n);
	used[n] = 1;
	while(!q.empty()) {
		int u = q.top();
		cout << u << endl;
		if(u == 1 || (u-1)%b == 0) {
			cout << "Yes" << endl;
			return ;
		}
		q.pop();
		while(u%a == 0 && !used[u/a]) {
			u /= a;
			q.push(u);
			used[u] = 1;
		}
		while(u-b > 0 && !used[u-b] && (u-b)%n) {
			u -= b;
			q.push(u);
			used[u] = 1;
		}
	}
	cout << "No" << endl;
}

int main() {
	int t;
	cin >> t;
	while(t--) {
		solve();
	}
	return 0;
}