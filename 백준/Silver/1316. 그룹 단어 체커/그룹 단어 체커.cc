#include <stdio.h>
#include <string.h>

int main()
{
	char str[100];
	int n;
	scanf("%d", &n);

	int count = n;

	for (int i = 0; i < n; i++)
	{
		char first = '0';
		int alphabet[26] = { 0, };
		scanf("%s", str);

		for (int j = 0; str[j] != NULL; j++)
		{
			if (first != str[j])	// 연속하지 않은 새로운 문자가 나왔을 때
			{
				first = str[j];
				alphabet[str[j] - 'a']++;
			}
			if (alphabet[str[j] - 'a'] == 2)	// 같은 문자가 묶이지 않고 떨어져 나옴
			{
				count--;
				break;	// 바로 다음 단어로
			}
		}
	}
	printf("%d", count);

	return 0;
}