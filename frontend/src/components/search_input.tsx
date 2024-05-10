import { ChangeEvent, FormEvent, useEffect, useState } from 'react'
import { ReactComponent as RefreshIcon } from 'images/refresh_icon.svg'
import { ReactComponent as SearchIcon } from 'images/search_icon.svg'
import { ReactComponent as ArrowIcon } from 'images/arrow_icon.svg'
import { AppStatus } from 'store/provider'

export default function SearchInput({ onSearch, value, appStatus }) {
  const [query, setQuery] = useState<string>(value)
  const handleSubmit = (event: FormEvent) => {
    event.preventDefault()
    if (!!query.length) {
      onSearch(query)
    }
  }
  const handleChange = (event: ChangeEvent<HTMLInputElement>) =>
    setQuery(event.target.value)

  useEffect(() => {
    setQuery(value)
  }, [value])

  return (
    <form className="w-full" onSubmit={handleSubmit}>
      <div className="relative mt-1 flex w-full items-center h-14 gap-2">
        <input
          type="search"
          className={`hover:border-green-500 outline-none focus-visible:border-green-600 w-full h-14 rounded-md border-2 border-zinc-300 px-3 py-2.5 pl-12 text-base font-medium placeholder-gray-400 ${
            appStatus === AppStatus.Idle ? 'pr-20' : 'pr-40'
          }`}
          value={query}
          onChange={handleChange}
          placeholder="What do you want to learn about herbs?"
        />
        <span className="pointer-events-none absolute left-4">
          <SearchIcon />
        </span>
        {appStatus === AppStatus.Idle ? (
          <button
            className="hover:bg-green disabled:bg-green-400 px-4 py-2 bg-green-500 rounded flex items-center absolute right-2 z-10"
            type="submit"
            disabled={!query.length}
          >
            <ArrowIcon width={24} height={24} />
          </button>
        ) : (
          <button
            className="hover:bg-green-400 hover:text-green-100 px-4 py-2 bg-green-100 rounded flex justify-center items-center text-green-400 font-bold absolute right-2 z-10"
            type="submit"
          >
            <span className="mr-2">
              <RefreshIcon width={24} height={24} />
            </span>
            Start over
          </button>
        )}
      </div>
    </form>
  )
}
