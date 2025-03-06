#include <stdio.h>

int max(x, y) {
	return (x) > (y) ? (x) : (y);
}

int main() {
	int a, b, c;
	int res = 0;

	scanf("%d %d %d", &a, &b, &c);
	
	if (a == b && b == c && c == a)
		res = a * 1000 + 10000;
	else {
		if (a == b)
			res = a * 100 + 1000;
		else if (b == c)
			res = b * 100 + 1000;
		else if (c == a)
			res = c * 100 + 1000;
		else {
			res = (max(a, max(b, c)) * 100);
		}	
	}
	
	printf("%d\n", res);

	return 0;
}