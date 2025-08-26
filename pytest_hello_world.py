#include <stdio.h>
#include <stdlib.h>

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/semphr.h"


SemaphoreHandle_t xBinarySemaphore1 = NULL;
SemaphoreHandle_t xBinarySemaphore2 = NULL;
SemaphoreHandle_t xBinarySemaphore3 = NULL;

void Task1(void *pvParameters)
{
    while (1) 
    {
        // Espera o semáforo 1 para rodar
        if (xSemaphoreTake(xBinarySemaphore1, portMAX_DELAY) == pdTRUE) 
        {
            printf("[Tarefa 1] Executou - Matheus-Enzo\n");
        }
        vTaskDelay(pdMS_TO_TICKS(1000)); // Delay de 1 segundo
    }
}

void Task2(void *pvParameters)
{
    while (1) 
    {
        // Espera o semáforo 2 para rodar
        if (xSemaphoreTake(xBinarySemaphore2, portMAX_DELAY) == pdTRUE) 
        {
            printf("[Tarefa 2] Executou - Matheus-Enzo\n");
        }
        vTaskDelay(pdMS_TO_TICKS(1000)); // Delay de 1 segundo
    }
}

void Task3(void *pvParameters)
{
    while (1) 
    {
        // Espera o semáforo 3 para rodar
        if (xSemaphoreTake(xBinarySemaphore3, portMAX_DELAY) == pdTRUE) 
        {
            printf("[Tarefa 3] Executou - Matheus-Enzo\n");
        }
        vTaskDelay(pdMS_TO_TICKS(1000)); // Delay de 1 segundo
    }
}

void app_main(void)
{
    // Criação dos semáforos binários
    xBinarySemaphore1 = xSemaphoreCreateBinary();
    xBinarySemaphore2 = xSemaphoreCreateBinary();
    xBinarySemaphore3 = xSemaphoreCreateBinary();

    if (xBinarySemaphore1 == NULL || xBinarySemaphore2 == NULL || xBinarySemaphore3 == NULL) 
    {
        printf("Falha ao criar semáforo binário\n");
        return;
    }

    // Inicializando os semáforos para que a Tarefa 1 comece a execução primeiro
    xSemaphoreGive(xBinarySemaphore1);

    // Criação das tarefas
    xTaskCreate(Task1, "Task1", 2048, NULL, 5, NULL);
    xTaskCreate(Task2, "Task2", 2048, NULL, 5, NULL);
    xTaskCreate(Task3, "Task3", 2048, NULL, 5, NULL);

    // Intercalando os semáforos para permitir que as tarefas executem de forma alternada
    while (1) 
    {
        xSemaphoreGive(xBinarySemaphore1); // Libera o semáforo 1 para a Tarefa 1
        vTaskDelay(pdMS_TO_TICKS(1000)); // Delay de 1 segundo

        xSemaphoreGive(xBinarySemaphore2); // Libera o semáforo 2 para a Tarefa 2
        vTaskDelay(pdMS_TO_TICKS(1000)); // Delay de 1 segundo

        xSemaphoreGive(xBinarySemaphore3); // Libera o semáforo 3 para a Tarefa 3
        vTaskDelay(pdMS_TO_TICKS(1000)); // Delay de 1 segundo

        // Espera até que as tarefas possam ser executadas novamente
    }
}
