
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <unistd.h>  // For sleep()

const char lowercase[] = "abcdefghijklmnopqrstuvwxyz";
const char uppercase[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const char digits[] = "0123456789";
const char symbols[] = "!@#$%^&*()_+-=[]{}|;:',.<>?/";

void bruteForce(const char *target, const char *pool) {
    int len = strlen(target);
    char guess[len + 1];
    guess[len] = '\0';

    while (1) {
        for (int i = 0; i < len; i++) {
            guess[i] = pool[rand() % strlen(pool)];
        }

        printf("Trying: %s\n", guess);
        sleep(1);  // Simulate slow brute-force

        if (strcmp(guess, target) == 0) {
            printf("Password cracked: %s\n", guess);
	    FILE *f = fopen("result.txt", "w");
fprintf(f, "Password cracked: %s\n", guess);
fprintf(f, "Attempts: %d\n", attempts);
fprintf(f, "Time: %ld seconds\n", end - start);
fclose(f);
            break;
        }
    }
}

int main() {
    srand(time(NULL));
    char password[20];
    int choice;

    printf("Enter your password: ");
    scanf("%s", password);

    printf("\nChoose character type combination:\n");
    printf("1. Lowercase only\n");
    printf("2. Uppercase only\n");
    printf("3. Digits only\n");
    printf("4. Symbols only\n");
    printf("5. Lowercase + Uppercase\n");
    printf("6. Lowercase + Digits\n");
    printf("7. Lowercase + Symbols\n");
    printf("8. Uppercase + Digits\n");
    printf("9. Uppercase + Symbols\n");
    printf("10. Symbols + Digits\n");
    printf("11. All combined\n");
    printf("Enter option: ");
    scanf("%d", &choice);

    char pool[100] = "";
    switch (choice) {
        case 1: strcpy(pool, lowercase); break;
        case 2: strcpy(pool, uppercase); break;
        case 3: strcpy(pool, digits); break;
        case 4: strcpy(pool, symbols); break;
        case 5: strcpy(pool, lowercase); strcat(pool, uppercase); break;
        case 6: strcpy(pool, lowercase); strcat(pool, digits); break;
        case 7: strcpy(pool, lowercase); strcat(pool, symbols); break;
        case 8: strcpy(pool, uppercase); strcat(pool, digits); break;
        case 9: strcpy(pool, uppercase); strcat(pool, symbols); break;
        case 10: strcpy(pool, symbols); strcat(pool, digits); break;
        case 11: strcpy(pool, lowercase); strcat(pool, uppercase); strcat(pool, digits); strcat(pool, symbols); break;
        default: printf("Invalid choice.\n"); return 1;
    }

    bruteForce(password, pool);
    return 0;
}
