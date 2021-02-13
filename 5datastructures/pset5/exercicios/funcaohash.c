#include <glib.h>

                GStringChunk;
GStringChunk *  g_string_chunk_new         (gsize size);
gchar*          g_string_chunk_insert      (GStringChunk *chunk, const gchar *string);
gchar*          g_string_chunk_insert_const(GStringChunk *chunk, const gchar *string);
gchar*          g_string_chunk_insert_len  (GStringChunk *chunk, const gchar *string, gssize len);
void            g_string_chunk_clear       (GStringChunk *chunk);
void            g_string_chunk_free        (GStringChunk *chunk);


//Os pedaços de palavra são usados ​​para armazenar grupos de palavras. 
//A memória é alocada em blocos e, à medida que as palavras são adicionadas 
//ao GStringChunk, elas são copiadas para a próxima posição livre em um bloco.
//Quando um bloco está cheio, um novo bloco é alocado.

//Ao armazenar um grande número de palavras, os blocos de palavras são mais 
//eficientes do que usar g_strdup (), pois são necessárias menos chamadas 
//para malloc () e menos memória é desperdiçada nas despesas gerais de alocação
//de memória.

//Adicionando strings com g_string_chunk_insert_const (), também é possível 
//remover duplicatas.

//Para criar um novo GStringChunk, use g_string_chunk_new ().

//Para adicionar seqüências de caracteres a um GStringChunk, 
//use g_string_chunk_insert ().

//Para adicionar seqüências de caracteres a um GStringChunk, mas sem duplicar 
//as seqüências que já estão no GStringChunk, use g_string_chunk_insert_const ().

//Para liberar o GStringChunk inteiro, use g_string_chunk_free (). Não é possível 
//liberar seqüências individuais.

typedef struct _GStringChunk GStringChunk;

//Uma estrutura de dados opaca representando pedaços de cadeia. Só deve ser acessado 
//usando as seguintes funções.
_____________________________________________________________________________________

GStringChunk *      g_string_chunk_new                  (gsize size);
Creates a new GStringChunk.

//Tamanho :

//o tamanho padrão dos blocos de memória alocados para armazenar as seqüências de 
//caracteres. Se uma sequência específica for maior que esse tamanho padrão, um bloco 
//maior de memória será alocado para ela.
//Devoluções:

//um novo GStringChunk
_____________________________________________________________________________________

g_string_chunk_insert ()
gchar *             g_string_chunk_insert               (GStringChunk *chunk,
                                                         const gchar *string);

//Adiciona uma cópia da string ao GStringChunk. Retorna um ponteiro para a nova cópia 
//da sequência no GStringChunk. Os caracteres na sequência podem ser alterados, se 
//necessário, embora você não deva alterar nada após o final da sequência.

//Diferentemente de g_string_chunk_insert_const (), esta função não verifica se há 
//duplicatas. Também as strings adicionadas com g_string_chunk_insert () não serão 
//pesquisadas por g_string_chunk_insert_const () ao procurar duplicatas.

//pedaço: um GStringChunk
//palavra : a string a ser adicionada
//Devoluções: um ponteiro para a cópia da sequência dentro do GStringChunk
_____________________________________________________________________________________

g_string_chunk_insert_len ()
gchar *             g_string_chunk_insert_len           (GStringChunk *chunk,
                                                         const gchar *string,
                                                         gssize len);

//Adiciona uma cópia dos primeiros bytes de len da string no GStringChunk. A cópia é 
//nula-terminada.
//Como essa função não para em bytes nulos, é responsabilidade do chamador garantir 
//que a sequência tenha pelo menos bytes endereçáveis.
//Os caracteres na sequência retornada podem ser alterados, se necessário, embora você 
//não deva alterar nada após o final da sequência.

//pedaço: um GStringChunk
//palavra : bytes para inserir
//len: número de bytes de sequência a inserir ou -1 para inserir uma sequência 
//terminada em nulo.
//Devoluções: um ponteiro para a cópia da sequência dentro do GStringChunk
_____________________________________________________________________________________

g_string_chunk_clear ()
void                g_string_chunk_clear                (GStringChunk *chunk);


//Libera todas as seqüências contidas no GStringChunk. Depois de chamar 
g_string_chunk_clear (), //não é seguro acessar nenhuma das strings contidas nela.

//pedaço: um GStringChunk
_____________________________________________________________________________________

g_string_chunk_free ()
void                g_string_chunk_free                 (GStringChunk *chunk);


//Libera toda a memória alocada pelo GStringChunk. Após chamar g_string_chunk_free (),
//não é seguro acessar nenhuma das strings que estavam contidas nela.
//pedaço: um GStringChunk
_____________________________________________________________________________________
