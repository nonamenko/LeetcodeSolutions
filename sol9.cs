public class Solution {
    public bool IsPalindrome(int x) {
        if (x < 0)
            return false;
        
        if (x / 10 == 0)
            return true;
        
        var x0 = x;
        var y = 0;
        
        while (x0 > 0) {
            y = y * 10 + x0 % 10;
            x0 = x0 / 10;
        }
        
        return x == y;
    }
}