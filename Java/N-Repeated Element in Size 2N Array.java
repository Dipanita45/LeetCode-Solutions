class Solution {
    public int repeatedNTimes(int[] nums) {
        Map<Integer,Integer> freq=new HashMap<>();
        for(int z:nums){
            freq.put(z,freq.getOrDefault(z,0)+1);
        }

        for(int k:freq.keySet())
            if(freq.get(k)>1){
                return k;
            }
            throw null;
        }
}
