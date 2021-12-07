#include <stdio.h>
#include <time.h>

//Insertion sort

void display (int arr[] , int l){
    for (int i = 0; i < l; i++){
        printf("%d  ",arr[i]);
    }
    printf("\n");
}

int main(){

    clock_t tim;
    tim = clock();
    
    int arr[8] = {9,2,7,5,1,4,3,6} , var , j;
    //sorting in increasing order 
    int len_ = sizeof(arr)/sizeof(arr[0]);
    printf("Array before sorrting:\n");
    display(arr , len_);

    for (int i = 0; i < len_ ; i++){
        var = arr[i];
        j = i-1;
        if (j > -1){
            while (var < arr[j] && j > -1){
                arr[j+1] = arr[j];
                j -= 1;
            }
            arr[j+1] = var;
        }
    }

    display(arr,len_);

    tim = clock() - tim;
    double total_time = ((double)tim)/CLOCKS_PER_SEC;
    printf("Time taken:%lfs \n",total_time);
 
    return 0;
}