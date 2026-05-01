// import java.util.*;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        List<Integer> arr = new ArrayList<>();

        for (int i = 0; i < k; i++) {
            pq.add(nums[i]);
        }

        arr.add(pq.peek());

        for (int i = k; i < nums.length; i++) {
            pq.remove(nums[i - k]);   // remove outgoing
            pq.add(nums[i]);         // add incoming
            arr.add(pq.peek());
        }

        // convert list → array
        int[] res = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            res[i] = arr.get(i);
        }

        return res;
    }
}