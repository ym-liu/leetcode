char *mergeAlternately(char *word1, char *word2)
{
    // get both word lengths
    int word1Len = strlen(word1);
    int word2Len = strlen(word2);

    // differentiate shortest from longest word
    char *shortestWord = (word1Len <= word2Len) ? word1 : word2;
    char *longestWord = (word1Len > word2Len) ? word1 : word2;
    int shortestWordLen = strlen(shortestWord);
    int longestWordLen = strlen(longestWord);

    // allocate space for new word
    char *newWord = (char *)malloc(sizeof(char) * (word1Len + word2Len + 1));

    // merge alternately up until shortest word length
    for (int i = 0; i < shortestWordLen; i++)
    {
        newWord[2 * i] = word1[i];
        newWord[2 * i + 1] = word2[i];
    }
    // append the rest of the longest word behind
    for (int j = 0; j < longestWordLen - shortestWordLen; j++)
    {
        newWord[2 * shortestWordLen + j] = longestWord[shortestWordLen + j];
    }
    // add null terminator to the string
    newWord[word1Len + word2Len] = '\0';

    return newWord;
}