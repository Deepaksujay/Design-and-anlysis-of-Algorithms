#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int check_sorted(int arr[], int l){
    for (int i = 1; i < l; i++){
        if (arr[i] < arr[i-1]){
            return 0;
        }
    }
    return 1;
}

void display(int arr[], int l){
    for (int i = 0; i < l; i++){
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

int search(int arr[] , int ele , int len , int start , int end , int check){
    int mid = (end + start)/2;
    
    if (mid == check){
        if (mid == len - 2){
            if (arr[mid + 1] == ele){
                printf("Element is found!\n");
                return 1;
            }
        }
        printf("Element is not found :/\n");
        return 0;
    }

    if (ele == arr[mid]){
        printf("Element is found!\n");
    }
    else if (ele > arr[mid]){
        return search(arr,ele,len,mid,end,mid);
    }
    else if (ele < arr[mid]){
        return search(arr,ele,len,start,mid,mid);
    }
    return 1;
}

int main(){

    clock_t tim;
    tim = clock();
    
    int arr[7] = {-81,-23,0,2,8,11,23};
    int len_ = sizeof(arr)/sizeof(arr[0]) , ele;
    //check_sorted(arr,len_)
    if (check_sorted(arr,len_)){
        printf("Enter the element you want to search: ");
        scanf("%d",&ele);
        search(arr,ele,len_,0,(len_ - 1),len_);
    }
    else{
        sort(arr,0,len_-1);
        printf("Enter the element you want to search: ");
        scanf("%d",&ele);
        search(arr,ele,len_,0,(len_ - 1),len_);
    }

    tim = clock() - tim;
    double total_time = ((double)tim)/CLOCKS_PER_SEC;
    printf("Time taken:%lfs \n",total_time);
 
    return 0;
}