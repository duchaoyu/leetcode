class Solution
{
public:
    vector<int> runningSum(vector<int> &nums)
    {
        int i = 1;
        while (i < nums.size())
        {
            nums[i] += nums[i - 1];
            i++;
        }
        return nums;
    }
};

/* note:
vector<int> runningSum(vector<int>& nums) {
    partial_sum(begin(nums), end(nums), begin(nums));
    return nums;
}
*/
