#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void display (int arr[] , int l){
    for (int i = 0; i < l; i++){
        printf("%d  ",arr[i]);
    }
    printf("\n");
}

void bubble_sort(int arr[],int len){
    int l;
    while (l){
        l=0;
        for(int i=1;i<len; i++){
            if(arr[i] < arr[i-1]){
                arr[i] = arr[i] + arr[i-1];
                arr[i-1] = arr[i] - arr[i-1];
                arr[i] = arr[i] - arr[i-1];
                l++;
            }
        }
    }
}

int main(){

    clock_t tim;
    tim = clock();
    
    int arr[8] = {9,2,7,5,1,4,3,6} , leng;
    leng = sizeof(arr)/sizeof(arr[0]);
    display(arr,leng);
    bubble_sort(arr,leng);
    display(arr,leng);

    tim = clock() - tim;
    double total_time = ((double)tim)/CLOCKS_PER_SEC;
    printf("Time taken:%lfs \n",total_time);
 
    return 0;
}