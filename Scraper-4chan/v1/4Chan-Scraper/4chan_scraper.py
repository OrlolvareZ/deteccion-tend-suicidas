#!usr/bin/env python3
# -*- coding: utf-8 -*-

# Dependencies
from datetime import datetime
import traceback
import urllib.request
import basc_py4chan
import argparse
import shutil
import timeit
import tqdm
import json
import csv
import requests
import os


def download_file(url, destination, filename):
    """Descarga un archivo desde la URL dada hacia el destino especificado con el nombre de archivo proporcionado."""
    try:
        response = requests.get(url)
        full_path = os.path.join(destination, filename)
        with open(full_path, 'wb') as file:
            file.write(response.content)
        print(f"Archivo descargado: {filename}")
    except Exception as e:
        print(f"Error al descargar el archivo: {filename}")
        print(str(e))


def write_file_data(post, filepath):
    """Obtiene metadatos de archivo de una publicación de 4Chan / Descargador de archivos"""
    with open(filepath, 'a', encoding='utf-8') as f:
        if post.has_file:
            f.write((f'Nombre de archivo: {post.filename}\n'
                     f'Tamaño del archivo: {post.file_size} bytes\n'
                     f'Hash MD5: {post.file_md5_hex}\n'
                     f'URL del archivo: {post.file_url}\n'
                     f'URL de miniatura: {post.thumbnail_url}\n\n'))
            # Extrae el nombre de archivo de file_url
            filename = post.file_url.split('/')[-1]
            # Descarga el archivo usando la función download_file
            try:
                download_file(post.file_url, images_dir, filename)
            except Exception as e:
                print(f"Error al descargar el archivo: {filename}")
                print(str(e))
        f.close()


def get_board_info(board_name):
    """Gets Board Information of a given 4Chan Board"""
    board = basc_py4chan.Board(board_name)
    board.refresh_cache(if_want_update=True)
    # CLI argument for number of threads to scrape
    all_thread_ids = board.get_all_thread_ids()
    board_metadata = (f'Board Title: {board.title}\n'
                      f'Number of Threads Currently: {len(all_thread_ids)}\n'
                      f'Number of Threads to Scrape: {args.num_threads}\n')
    return board, all_thread_ids, board_metadata


def write_thread_data(thread, filepath):
    """Gets information about a given 4Chan thread"""
    if thread.expand() != None:
        thread.expand()
    if thread.update(force=True) != None:
        num_new_posts = thread.update(force=True)
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write((f"Thread ID: {thread_id}\n"
                 f"Sticky?: {thread.sticky if thread.sticky != None else 'None'}\n"
                 f"Closed?: {thread.closed}\n"
                 f"Archived: {thread.archived}\n"
                 f"Number of Posts on Thread: {len(thread.posts)}\n"
                 f"JSON URL: {basc_py4chan.Url('pol').thread_api_url(thread_id)}\n"
                 f"Number of Replies on Thread: {len(thread.replies)}\n"
                 f"Number of New Posts: {num_new_posts if num_new_posts > 0 else 0}\n"))




def write_file_data(post, filepath):
    """Gets File Metadata of a given 4Chan Post / File Downloader"""
    with open(filepath, 'a', encoding='utf-8') as f:
        if post.has_file:
            f.write((f'Filename: {post.filename}\n'
                     f'File Size: {post.file_size} bytes\n'
                     f'MD5 Hash: {post.file_md5_hex}\n'
                     f'File URL: {post.file_url}\n'
                     f'Thumbnail URL: {post.thumbnail_url}\n\n'))
        f.close()


def make_safe_filename(string):
    """Creates a string safe for file naming conventions"""
    def safe_char(c): return c if c.isalnum() else "_"
    return "".join(safe_char(c) for c in string).rstrip("_")


def download_json_thread(local_filename, url):
    """Download the given JSON file, and pretty-print before outputted"""
    with open(local_filename, 'w', encoding='utf-8') as json_file:
        try:
            thread_json_data = json.loads(urllib.request.urlopen(url).read())
            json_file.write(json.dumps(thread_json_data,
                            sort_keys=False, indent=4, separators=(',', ': ')))
            json_file.close()
        except Exception as e:
            if args.debug == 'True' or args.debug == 'true':
                print(f'Error downloading {local_filename}.\n')


def mkdir(path, mode):
    """Makes a directory within the filesystem"""
    try:
        if not (os.path.exists(path)):
            os.mkdir(path, mode)
        else:
            if args.debug == 'True' or args.debug == 'true':
                print(f'"{path}" already created.')
    except Exception as e:
        if args.debug == 'True' or args.debug == 'true':
            print(f'Failed to create directory {path}.\n')


def archive_data(board_name, board_name_dir):
    """Compress data to .zip and remove original folder"""
    try:
        if args.debug == 'True' or args.debug == 'true':
            print('\nCompressing Data...')
        shutil.make_archive(
            f'{board.name} - {datetime.now().strftime("%b-%d-%Y  %H-%M-%S")}', 'zip', f'{board_name_dir}')
        shutil.rmtree(f'{board_name_dir}')
        if args.debug == 'True' or args.debug == 'true':
            print('Data compressed!')
    except Exception as e:
        if args.debug == 'True' or args.debug == 'true':
            print('Error compressing data.\n')


def write_comments_csv(post, filepath):
    """Create CSV and writes 4Chan comments and replies to it"""
    comment = post.text_comment.encode('utf-8').decode('utf-8')
    with open(filepath, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if os.stat(filepath).st_size == 0:
            writer.writerow(['post_id', 'date_time', 'subject',
                            'comment/reply', 'name', 'is_op?', 'url'])
        writer.writerow([post.post_id, post.datetime.strftime("%b-%d-%Y, %H:%M:%S"), post.subject if post.subject != None else 'No Subject',
                         '(REPLY) ' + comment if ">>" in comment and not (post.is_op) else comment, post.name.encode(
                             'utf-8').decode('utf-8') if post.name != None else 'No Name',
                         post.is_op, post.semantic_url])
    f.close()


# TODO:
    # Multithread --> not too important rn
    # Update a thread folder if new data is there ---> important
    # possible bugs with duplicate folders?

if __name__ == "__main__":
    # Parse CLI for Board Name / Toggle Debugging
    parser = argparse.ArgumentParser()
    parser.add_argument("--board_name", type=str,
                        help="4Chan Board Name", required=True, default='pol')
    parser.add_argument("--num_threads", type=int,
                        help="Number of threads to scrape on 4Chan Board", required=True, default=10)
    parser.add_argument('--feature', dest='feature', action='store_true')
    parser.add_argument('--no-feature', dest='feature', action='store_false')
    parser.add_argument("--debug", type=str, help="Turn debugging on", required=False,
                        default='False', choices=['True', 'False', 'true', 'false'])
    args = parser.parse_args()

    # Get Board Information and Begin Scrape
    try:
        board, all_thread_ids, board_metadata = get_board_info(args.board_name)
        print(f'\nBeginning 4Chan Catalog Scrape on /{board.name}/',
              '\n---------------------------------------')
        print('Current Date and Time:',
              datetime.now().strftime("%b-%d-%Y, %H:%M:%S"))

        # Defining file structure paths
        board_name_dir = f'{board.name}/'

        # Print Board Information
        print(board_metadata)
        if args.num_threads and (args.num_threads <= 0 or args.num_threads > len(all_thread_ids)):
            parser.error(
                f"Number of threads not in range: {[1, len(all_thread_ids)]}\n")

        print('Processing...\n')

        if args.debug == 'True' or args.debug == 'true':
            print('Subject Names Scraped:\n-------------------------')

        # Start runtime execution timer
        start = timeit.default_timer()

        # Create directory for board name
        mkdir(board_name_dir, 0o0666)

        # Check if a given thread is not 404'd
        if board.thread_exists:
            # Loop for each thread in the thread ID list
            for thread_id in tqdm.tqdm(all_thread_ids[0: args.num_threads], desc='Scraping Progress'):
                thread = board.get_thread(thread_id)

                # Defining additional file structure paths
                if thread.posts != None:
                    subject = thread.posts[0].subject
                    if args.debug == 'True' or args.debug == 'true':
                        print("\n\n" + subject if subject !=
                              None else '\n\nNo Subject')
                    if subject != None:
                        thread_id_dir = f'{board.name}/{thread_id} - {make_safe_filename(subject)}'
                    else:
                        thread_id_dir = f'{board.name}/{thread_id} - No Subject'

                    images_dir = f'{thread_id_dir}/{thread_id} files/'

                # Create directory structure for thread
                mkdir(thread_id_dir, 0o0666)
                mkdir(images_dir, 0o0666)

                # Download JSON for thread via catalog URL
                json_url = basc_py4chan.Url(
                    args.board_name).thread_api_url(thread_id)
                download_json_thread(
                    f'{thread_id_dir}/{thread_id}.json', json_url)

                # Write thread information to .txt
                write_thread_data(
                    thread, f'{thread_id_dir}/{thread_id} - thread metadata.txt')

                # Post Information
                if thread.posts != None:
                    for post in thread.posts:

                        # Write comments and replies to CSV file
                        write_comments_csv(
                            post, f'{thread_id_dir}/{thread_id} - comments & replies.csv')

                        # Write file metadata to .txt
                        if post.has_file:
                            write_file_data(
                                post, f'{thread_id_dir}/{thread_id} - file metadata.txt')
                            download_file(post, post.file_url,
                                          f'{images_dir}' + post.filename)

        # Zip up and remove board name folder
        archive_data(board.name, board_name_dir)
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting...")
        exit()
    except Exception as e:
        traceback.print_exc()
        print(f"\nAn error occurred: {str(e)}")
        print(f"Deleting /{board.name}/ folder in {os.getcwd()}.")
        shutil.rmtree(f'{board_name_dir}')
        exit(f'{board.name} folder successfully removed. Please rerun the script.')
    # Finish scraping / end runtime execution timer
    end = timeit.default_timer()
    print('\nScraping Complete!')
    print("Total Runtime Execution:", round(end - start, 3), "seconds")
