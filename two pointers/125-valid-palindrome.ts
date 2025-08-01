function isPalindrome(s: string): boolean {
    // convert input string to lowercase and remove all non-alphanumeric chars
    const cleanedString: string = s.toLowerCase().replace(/[^a-z0-9]/g, "");

    // go char-by-char, check if not palindrome
    const n: number = cleanedString.length;
    for (let i: number = 0; i < Math.floor(n / 2); i++) {
        if (cleanedString[i] != cleanedString[n - i - 1]) return false;
    }

    return true;
}