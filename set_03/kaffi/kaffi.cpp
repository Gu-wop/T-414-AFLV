#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

inline bool canFitWithMaxHeight(const vector<int> &chairCounts, int w, int maxHeight)
{
    int stacksNeeded = 0;
    for (int count : chairCounts)
    {
        stacksNeeded += (count + maxHeight - 1) / maxHeight;
        if (stacksNeeded > w)
            return false;
    }
    return true;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, w;
    cin >> n >> w;

    vector<int> chairCounts(n);
    int totalChairs = 0;
    int maxCount = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> chairCounts[i];
        totalChairs += chairCounts[i];
        maxCount = max(maxCount, chairCounts[i]);
    }

    int left = 1, right = maxCount;

    while (left < right)
    {
        int mid = left + (right - left) / 2;
        if (canFitWithMaxHeight(chairCounts, w, mid))
        {
            right = mid;
        }
        else
        {
            left = mid + 1;
        }
    }

    int maxHeight = left;
    int disorganization = w * maxHeight - totalChairs;

    cout << disorganization << '\n';

    return 0;
}