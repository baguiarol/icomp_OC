
#include <stdio.h>
#include <stdlib.h>

#define ELEMENTS 1000

//(sudo perf stat -e cache-misses,cache-references ./not_friendly 250 /dev/null) > out 2>&1 && cat out | grep cache-misses >> run250.txt

int main(int argc, char *argv[]){
    int INTERVAL = atoi(argv[1]);

    if(INTERVAL < 1|| INTERVAL > 1000){
        printf("Erro: escolha um argumento de entrada entre 1 e 1000\n");
        return 0;
    }

    int *arr = (int *) calloc(ELEMENTS*INTERVAL, sizeof(int));
    int i, sum = 0, iterations = 0;

    if(arr == NULL){
        printf("Memoria insuficiente.\n");
        exit(0);
    }
    
    for(i=0; i< ELEMENTS*INTERVAL; i+= INTERVAL){
        sum += (arr[i] + 5);
        iterations ++;
    }

    printf("Sum: %d; Iterations: %d\n", sum, iterations);
    free(arr);

    return 0;
}
