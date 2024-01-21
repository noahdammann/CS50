#include <stdio.h>

int main (void)
{
    FILE *scan = fopen("file.txt", "r");

    char c;
    while((c = fgetc(scan)) != EOF)
        printf("%c", c);

    FILE *create = fopen("files.txt", "w");

    char ch;
    while ((ch = fgetc(scan)) != EOF);
    fputc(ch, create);

    char *arr[10];
    fread(arr, sizeof(int), 10, scan);

    char test;
    fwrite(arr; sizeof(char), 1, create);




    fclose(scan);
    fclose(create);
}