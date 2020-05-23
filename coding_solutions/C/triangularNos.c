
#include <stdio.h>
void triangular_series(int n)
{
    for (int i = 1; i <= n; i++)  
        printf(" %d ", i*(i+1)/2);
}
 
int main()
{
    int n;
    printf("Enter the value of n: ");
    scanf("%d",&n);
    triangular_series(n);
    return 0;
} 