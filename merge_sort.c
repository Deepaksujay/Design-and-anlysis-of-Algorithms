#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void display(int arr[] ,int start, int l){
    for (int i = start; i <= l; i++){
        printf("%d  ",arr[i]);
    }
    printf("\n");
}

void attaching (int arr[], int start, int middle, int end){
    int no_1 = middle - start + 1, no_2 = end - middle;
    int arr_1[no_1], arr_2[no_2];
    //printf("Before Merging : ");
    //display(arr,start,end);
    for (int i = 0; i < no_1; i++){
        arr_1[i] = arr[start + i];
    }
    for (int j = 0; j < no_2; j++){
        arr_2[j] = arr[middle + j + 1];
    }
    int i = 0, j = 0 ,l = start;
    while ( i < (no_1) && j < (no_2)){
        if (arr_1[i] < arr_2[j]){
            arr[l++] = arr_1[i++];
        }
        if (arr_1[i] > arr_2[j]){
            arr[l++] = arr_2[j++];
        }
        if (arr_1[i] == arr_2[j]){
            arr[l++] = arr_1[i++];
            arr[l++] = arr_2[j++];
        }
    }
    while (i < no_1){
        arr[l++] = arr_1[i++];
    }
    while (j < no_2){
        arr[l++] = arr_2[j++];
    }
    //printf("After merging : ");
    //display(arr,start,end);
}

void sort(int arr[], int start, int end){
    if (start < end){
        int middle = (start + end)/2;
        //printf("start: %d middle: %d end: %d array:  ",start,middle,end);
        //display(arr,start,end);
        sort(arr,start,middle);
        sort(arr,middle + 1,end);
        attaching(arr,start,middle,end);
    }
}

int main(){

    clock_t tim;
    tim = clock();
    srand(time(0));
    //int arr[8] = {9,2,7,5,1,4,3,6};
    //int len_ = sizeof(arr)/sizeof(arr[0]);
    printf("Enter the no of elements:");
    int len_ ;
    scanf("%d",&len_);
    int arr[len_];
    for (int i = 0; i < len_ ; i++){
        arr[i] = rand();
    }
    //display(arr,0,len_-1);
    sort(arr,0,len_-1);
    //display(arr,0,len_-1);

    tim = clock() - tim;
    double total_time = ((double)tim)/CLOCKS_PER_SEC;
    printf("Time taken:%lfs \n",total_time);
 
    return 0;
}