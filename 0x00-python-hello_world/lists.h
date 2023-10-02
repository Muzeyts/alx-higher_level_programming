#include <stdlib.h>

/**
 * struct listint_s - lst of linked
 * @n: numbers that are  integer
 * @next: to the next node to be pointed
 *
 */
typedef struct listint_s
{
        int n;
        struct listint_s *next;
} listint_t;

listint_t *add_nodeint(listint_t **head, const int n);
int check_cycle(listint_t *list);
size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);

#endif /* LISTS_H */

