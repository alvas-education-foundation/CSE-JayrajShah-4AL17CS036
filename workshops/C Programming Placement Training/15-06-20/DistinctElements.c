//Write a C program to count distinct elements in an array.

#include <stdio.h>
void distict_elements(int a[], int n);
int main()
{
    int size_array, i, arr[20];
    printf("Enter Array size \n");
    scanf("%d", &size_array);
    printf("Enter Array elements \n");
    for (i = 0; i < size_array; i++)
    {
        scanf("%d", &arr[i]);
    }
    distict_elements(arr, size_array);
    return 0;
}
void distict_elements(int a[], int n)
{
    int count = 0;
    int i, j;
    printf("Filered Array : \n");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < i; j++)
        {
            if (a[i] == a[j])
                break;
        }
        if (i == j)
        {
            count++;
            printf(" %d ", a[i]);
        }
    }
    printf("\n Number of distinct elemets : %d ", count);
}