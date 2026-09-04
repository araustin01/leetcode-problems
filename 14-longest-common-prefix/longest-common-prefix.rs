impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut result = String::new();
        if strs.len() < 1 { // guard against empty input
            return result;
        }
        
        let minimum_length = strs.iter().map(|s| s.len()).min().unwrap_or(0); // shortest string length from the list
        for i in 0..minimum_length {
            let c_byte: u8 = strs[0].as_bytes()[i]; // check byte ref
            for s in &strs { // check byte (char ref) against the other strings
                if s.as_bytes()[i] != c_byte { // failed check, early exit
                    return result;
                }
            }
            result.push(c_byte as char)
        }

        result
    }
}