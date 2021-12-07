#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void selection_sort(int arr[],int a,int b){ //a=start index for sort,b=end index for sort
    if (a != b){
        int temp,max_index = a;
        for(int i=a;i<=b;i++){
            if (arr[i] > arr[max_index]){
                max_index = i;
            }
        }
        if (b != max_index){
            arr[b] = arr[b] + arr[max_index];
            arr[max_index] = arr[b] - arr[max_index];
            arr[b] = arr[b] - arr[max_index];
        }
        selection_sort(arr,a,b-1);
    }
}

void display(int arr[],int n){
    for (int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
}

int main(){

    clock_t tim;
    tim = clock();

    int arr[8] = {9,2,7,5,1,4,3,6};
    int l = sizeof(arr)/sizeof(arr[0]);
    display(arr,l);
    selection_sort(arr,0,l-1);
    display(arr,l);

    tim = clock() - tim;
    double total_time = ((double)tim)/CLOCKS_PER_SEC;
    printf("Time taken:%lfs \n",total_time);
 
    return 0;
}