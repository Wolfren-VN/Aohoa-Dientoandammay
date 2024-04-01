#include <stdio.h>
#include <math.h>

int xuatSoChinhPhuong(int n)
{
    int count = 0;
    for(int i = n; i > 0; i--)
    {
        if((int)sqrt(i)==(float)sqrt(i))
        {
            count++;
            printf("%d ",i);
        }
        
    }
    
    return count;
}

int main(void){
    int n;
    
    printf("Nhap vao so nguyen n: ");
    scanf("%d",&n);
    
    int sl = xuatSoChinhPhuong(n);
    printf("\nCo %d so chinh phuong!",sl);
}
