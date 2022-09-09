/* Eat_more */
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef double db;

#define faster() ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define tester() int t; cin >> t; while(t--)
#define PI atan(1)*4
#define in INT_MAX
#define im INT_MIN
#define fi first
#define se second
#define vi vector <int>
#define vll vector <ll>
#define pii pair <int, int>
#define mii map <int, int>
#define mp(x, y) make_pair(x, y)
#define all(x) x.begin() x.end();
const int Mod = 1e9 + 7;
const int nMax = 1e5 + 1;

void test() {
	int n;
	cin >> n;
	if (!n) exit(0);
	vi a(n);
	for (int &i : a) cin >> i;
	int ans = 0;
	for (int i = 1; i < n-1; i++)
		if(a[i] > a[i-1] && a[i] > a[i+1])
			ans ++;
	cout << ans << endl;
}

int main() {
	faster();
	while(true)
		test();
	return 0;
}