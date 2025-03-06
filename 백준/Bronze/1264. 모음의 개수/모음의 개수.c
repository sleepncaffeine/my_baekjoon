#include <stdio.h>

int main() {
	char s[256] = {0};
	int cnt = 0;

	while (1) {
		gets(s);

		if (s[0] == '#')
			break;

		for (int i = 0; s[i] != '\0'; i++) {
			if (s[i] == 'A' || s[i] == 'a')
				cnt++;
			else if (s[i] == 'E' || s[i] == 'e')
				cnt++;
			else if (s[i] == 'I' || s[i] == 'i')
				cnt++;
			else if (s[i] == 'O' || s[i] == 'o')
				cnt++;
			else if (s[i] == 'U' || s[i] == 'u')
				cnt++;
		}
		printf("%d\n", cnt);
		cnt = 0;
	}

	return 0;
}