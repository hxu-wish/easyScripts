import json

csv_file_path = "/Users/hxu/Downloads/csvjson.json"


def read_json(path):
    total_before_call_api = 0
    total_api = 0
    total_before_render = 0
    count = 0

    with open(path) as jfile:
        all_data = json.load(jfile)
        for single_data in all_data:
            event_list = single_data["_arguments"]["event_list_json"]
            event_list_json = json.loads(event_list[0])
            for item in event_list_json:
                if item['event_id'] == '34408':
                    extra_info_json = json.loads(item['extra_info'])
                    before_send_request_time = int(extra_info_json['beforeSendRequestTime'])
                    after_get_response_time = int(extra_info_json['afterGetResponseTime'])
                    before_render_time = int(extra_info_json['beforeRenderTime'])

                    if before_send_request_time > 0 and after_get_response_time > 0 and before_render_time > 0:
                        total_before_call_api = total_before_call_api + before_send_request_time
                        total_api = total_api + after_get_response_time
                        total_before_render = total_before_render + before_render_time
                        count = count + 1

        print(f'Hi, count = {count} average time = {total_before_call_api / count}')
        print(f'Hi, count = {count} average time = {total_api / count}')
        print(f'Hi, count = {count} average time = {total_before_render / count}')



if __name__ == '__main__':
    read_json(csv_file_path)
