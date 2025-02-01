public class Solution {
    public int MyAtoi(string s) {
        var negativeDelte = 1;
        var isNumberFound = false;
        var start = 0;
        var finish = 0;
        
        for (var i = 0; i < s.Length; i++) {
            if (!char.IsDigit(s[i]) && isNumberFound)
                break;
            
            if (s[i] == '+') {
                isNumberFound = true;
                start = i + 1;
                finish = i;
                continue;
            }
            
            if (s[i] == '-') {
                isNumberFound = true;
                negativeDelte = -1;
                start = i + 1;
                finish = i;
                continue;
            }
            
            if (char.IsDigit(s[i])) {           
                if (!isNumberFound) {
                    isNumberFound = true;
                    start = i;
                    finish = i;
                }
                else {                    
                    finish++;     
                }
                
                continue;
            }
            
            if (s[i] != ' ')
                return 0;
        }
        
        if (s.Length <= start || !char.IsDigit(s[start]))
            return 0;
        
        if (int.TryParse(s.Substring(start, finish - start + 1), out var result)) {
            return result * negativeDelte;
        }
        
        return negativeDelte > 0 ? int.MaxValue : int.MinValue;
    }
}