#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a new node into a sorted singly linked list
 * @head: pointer to the pointer of the first node
 * @number: the number to be inserted in the new node
 * 
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *current, *prev;

new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);

new_node->n = number;
new_node->next = NULL;

if (*head == NULL || (*head)->n >= number)
{
new_node->next = *head;
*head = new_node;
return (new_node);
}

current = *head;
while (current != NULL && current->n < number)
{
prev = current;
current = current->next;
}

new_node->next = current;
prev->next = new_node;

return (new_node);
}
