import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    linked_pages = corpus[page]
    number_of_pages = len(corpus)

    # Set the odds of landing on each type of page (either random or linked)
    if len(linked_pages) == 0:
        random_page_odds = 1 / number_of_pages
        linked_page_odds = 0 
    else:
        random_page_odds = (1 - damping_factor) / number_of_pages
        linked_page_odds = damping_factor / len(linked_pages)

    # Create probability distribution dictionary
    probability_dictionary = {}

    for p in corpus:
        if p in linked_pages:
            probability_dictionary[p] = linked_page_odds + random_page_odds
        else:
            probability_dictionary[p] = random_page_odds

    return probability_dictionary


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    current_page = random.choice(list(corpus.keys()))
    pages_visited = {page: 0 for page in corpus.keys()}

    for _ in range(n):
        probabilities = transition_model(corpus, current_page, damping_factor)

        # Based on the probabilities dictionary, pick a random page
        pages = list(probabilities.keys())
        page_probs = list(probabilities.values())
        current_page = random.choices(pages, weights=page_probs, k=1)[0]
        pages_visited[current_page] += 1

    # Normalize the pages_visited dictionary
    for page in pages_visited:
        pages_visited[page] /= n

    return pages_visited


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Initialize page_rank and threshold value
    page_rank = {page: 1 / len(corpus) for page in corpus.keys()}
    threshold = 0.001 

    # Iterative process
    while True:
        new_page_rank = page_rank.copy()
        max_change = 0

        for page in new_page_rank:
            # Find all the pages that link to current page
            linking_pages = set()
            for p in corpus:
                if page in corpus[p]:
                    linking_pages.add(p)

            # Calculate the sum of PR(i) / NumLinks(i)
            sum_pagerank_over_numlinks = 0
            for i in linking_pages:
                num_links = len(corpus[i])
                pr = page_rank[i]
                sum_pagerank_over_numlinks += (pr / num_links) 

            # Calculate the new Page Rank
            new_page_rank[page] = (1 - damping_factor) / len(corpus) + damping_factor * sum_pagerank_over_numlinks
            max_change = max(max_change, abs(new_page_rank[page] - page_rank[page]))

        # Check to see if change is bigger than threshold
        if max_change < threshold:
            break

        # Update page_rank 
        page_rank = new_page_rank

    return page_rank

if __name__ == "__main__":
    main()
