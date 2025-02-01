public class Solution {
    public int Reverse(int x) {
        var negativeDelta = x < 0 ? -1 : 1;
        x *= negativeDelta;
        
        var charArray = x.ToString().ToCharArray();
        Array.Reverse(charArray);
        long.TryParse(new string(charArray), out var y);
        
        return y > int.MaxValue ? 0 : (int)y * negativeDelta;
    }
}