#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (!(cin >> T))
        return 0;
    string s;
    getline(cin, s); // consume endline after T

    while (T--)
    {
        getline(cin, s); // line may contain spaces
        int n = (int)s.size();
        vector<int> pi(n, 0);

        for (int i = 1; i < n; ++i)
        { // compute prefix-function
            int j = pi[i - 1];
            while (j > 0 && s[i] != s[j])
                j = pi[j - 1];
            if (s[i] == s[j])
                ++j;
            pi[i] = j;
        }

        cout << (n - pi[n - 1]) << '\n';
    }
    return 0;
}
