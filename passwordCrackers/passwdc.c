
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int usrPwd;
    printf("Enter your 4-digit password (numbers only): ");
    scanf("%d", &usrPwd);

    srand(time(NULL));

    int attempt = 0;
    while (attempt != usrPwd) {
        attempt = rand() % 10000; // Range 0000 to 9999
        printf("Trying: %04d\n", attempt);
    }

    printf("Password cracked: %04d\n", attempt);
    return 0;
}
