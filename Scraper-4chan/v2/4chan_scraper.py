#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Dependencies
from datetime import datetime
import traceback
import basc_py4chan
import argparse
import csv
import os
import re


def write_comments_csv(post, filepath):
    """Crea un archivo CSV y escribe los comentarios y respuestas de 4Chan en él"""
    comment = post.text_comment.encode('utf-8').decode('utf-8')
    comment = comment.split("\n", 1)[1].strip() if "\n" in comment else comment
    with open(filepath, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if os.stat(filepath).st_size == 0:
            writer.writerow(['date_time', 'comment/reply', 'name', 'url'])
        writer.writerow([post.datetime.strftime("%b-%d-%Y, %H:%M:%S"),
                         comment if ">>" in comment and not (
                             post.is_op) else comment,
                         post.name.encode(
                             'utf-8').decode('utf-8') if post.name is not None else 'No Name',
                         post.semantic_url])
    f.close()


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
    # Added argument for output directory
    # ---------------------------------------------------------------------------------------------
    parser.add_argument("--output_dir", type=str, help="Output directory for scraped data",
                        required=False, default='scraped_data')
    # ---------------------------------------------------------------------------------------------
    args = parser.parse_args()

    # Get Board Information and Begin Scrape
    try:
        board = basc_py4chan.Board(args.board_name)
        board.refresh_cache(if_want_update=True)
        print(f'\nBeginning 4Chan Catalog Scrape on /{board.name}/',
              '\n---------------------------------------')
        print('Current Date and Time:',
              datetime.now().strftime("%b-%d-%Y, %H:%M:%S"))

        # Defining file structure paths
        # Use board name as directory name if no output directory is specified

        try:
            board_name_dir = f'{args.output_dir}/{board.name}/'
        except:
            board_name_dir = f'{board.name}/'

        # Print Board Information
        board_metadata = (f'Board Title: {board.title}\n'
                          f'Number of Threads Currently: {len(board.get_all_thread_ids())}\n'
                          f'Number of Threads to Scrape: {args.num_threads}\n')
        print(board_metadata)

        if args.num_threads and (args.num_threads <= 0 or args.num_threads > len(board.get_all_thread_ids())):
            parser.error(
                f"Number of threads not in range: {[1, len(board.get_all_thread_ids())]}\n")

        print('Processing...\n')

        # Create directory for board name
        os.makedirs(board_name_dir, exist_ok=True)

        # Check if a given thread is not 404'd
        if board.thread_exists:
            # Loop for each thread in the thread ID list
            for thread_id in board.get_all_thread_ids()[0:args.num_threads]:
                thread = board.get_thread(thread_id)

                # Obtener el tema del hilo (subject) y eliminar caracteres no permitidos
                thread_subject = thread.topic.subject if thread.topic.subject is not None else 'Not Subject'
                thread_subject = re.sub(r'[<>:"/\\|?*]', '', thread_subject)

                # Defining additional file structure paths
                thread_dir = f'{board_name_dir}Thread-{thread_id}-{thread_subject}/'
                # thread_dir = re.sub(r'[<>:"/\\|?*]', '', thread_dir)
                os.makedirs(thread_dir, exist_ok=True)

                # Get all posts in the thread
                posts = thread.posts

                # Loop through each post in the thread
                for post in posts:
                    # Skip posts without a comment
                    if post.text_comment is None:
                        continue

                    # Write post data to CSV file
                    csv_filename = f'Thread-{thread_id}-{thread_subject}.csv'
                    csv_filename = re.sub(r'[<>:"/\\|?*]', '', csv_filename)
                    csv_filepath = os.path.join(thread_dir, csv_filename)
                    write_comments_csv(post, csv_filepath)

        print('\n---------------------------------------')
        print('Scrape Completed!')
        print('---------------------------------------')

    except Exception as e:
        print('Error Occurred:', str(e))
        traceback.print_exc()
