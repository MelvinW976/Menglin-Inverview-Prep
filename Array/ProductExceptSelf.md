# 前缀乘和后缀乘

# prefixProd[i] = prefixProd[i-1] * nums[i-1];
# postProd[len-i] = postProd[len-i-1] * nums[i];
后缀和也是要从前往后的，第一个是1，后面连乘
#  ans[i] = prefixProd[i] * postProd[len-i-1];   
```java
class Solution {
    // 1 1  2  6 24
    //24 24 12 4  1
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int[] prefixProd = new int[len+1];
        int[] ans = new int[len];
        prefixProd[0] = 1;
        for(int i = 1; i < len+1; i++){
            prefixProd[i] = prefixProd[i-1] * nums[i-1];
        } 
        int[] postProd = new int[len+1];
        postProd[0] = 1;
        for(int i = len-1; i >= 0; i--){
            postProd[len-i] = postProd[len-i-1] * nums[i];
        }
        for(int i = 0; i < len; i++) {
            ans[i] = prefixProd[i] * postProd[len-i-1];
        }
        return ans;
    }
}

```
