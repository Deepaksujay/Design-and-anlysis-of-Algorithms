#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int linear_search(int arr[], int ele, int size_){
    for (int i=0; i<size_; i++){
        if (arr[i] == ele){
            return 1;
        }
    }
    return 0;
}

int main(){

    clock_t tim;
    tim = clock();

    int arr[7] = {-81,-23,0,2,8,11,23};
    int size_ = sizeof(arr)/sizeof(arr[0]),ele;
    printf("Enter the Number you want to search:");
    scanf("%d",&ele);
    if (linear_search(arr,ele,size_)){
        printf("Element is present\n");
    }
    else{
        printf("Element is not present :/ \n");
    }

    tim = clock() - tim;
    double total_time = ((double)tim)/CLOCKS_PER_SEC;
    printf("Time taken:%lfs \n",total_time);

    return 0;
}