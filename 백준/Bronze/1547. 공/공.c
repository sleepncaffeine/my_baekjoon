#include <stdio.h>

int main() {
	int cnt = 0;
	int pos = 1;

	scanf("%d", &cnt);

	for (int i = 0; i < cnt; i++) {
		int x, y;
		scanf("%d %d", &x, &y);
		
		if (x == y)
			continue;
		else if (pos == x)
			pos = y;
		else if (pos == y)
			pos = x;
		else
			continue;
	}

	printf("%d\n", pos);

	return 0;
}