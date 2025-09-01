#include <iostream>
#include <string>
#include <vector>
using namespace std;

int compute_period(const string &s)
{
    int L = s.length();
    if (L == 0)
        return 0;
    vector<int> pi(L, 0);
    int j = 0;
    for (int i = 1; i < L; ++i)
    {
        while (j > 0 && s[i] != s[j])
        {
            j = pi[j - 1];
        }
        if (s[i] == s[j])
        {
            ++j;
        }
        pi[i] = j;
    }
    int border = pi[L - 1];
    if (border == 0)
        return L;
    return L - border;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int N;
    cin >> N;
    string dummy;
    getline(cin, dummy);
    for (int i = 0; i < N; ++i)
    {
        string s;
        getline(cin, s);
        cout << compute_period(s) << '\n';
    }
    return 0;
}