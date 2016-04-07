from itertools import islice


class ChunkingError(Exception):
    pass


def chunkify(things, this_chunk, chunks):
    if this_chunk > chunks:
        raise ChunkingError("this_chunk is greater than total chunks")

    size = len(things) / chunks
    big_chunks = len(things) % chunks
    start = size * (this_chunk-1)
    if big_chunks:
        if this_chunk <= big_chunks:  # this_chunk is a big chunk
            size += 1
            start += this_chunk-1
        else:
            start += big_chunks  # account for the extra 1 'thing' in each big_chunk

    end = start + size
    try:
        return things[start:end]
    except TypeError:
        return islice(things, start, end)
