function isSubsequence(s: string, t: string): boolean {
    if (s === "") return true; // edgecase: if s is empty string

    // iterate through each char in t,
    // check if it matches the next char in the subsequence s
    let sIdx: number = 0;
    for (let tChar of t) {
        if (tChar === s[sIdx]) {
            sIdx++; // increment to the next char in subsequence s
            if (sIdx === s.length) return true; // full subsequence s found in t
        }
    }

    return false;
}